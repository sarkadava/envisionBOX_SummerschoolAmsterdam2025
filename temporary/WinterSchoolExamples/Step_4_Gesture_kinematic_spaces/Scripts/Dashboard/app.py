import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import json
import os
from pathlib import Path
from flask import send_from_directory
from moviepy import VideoFileClip

app = Dash(__name__)

# Create videos_rerendered directory if it doesn't exist
if not os.path.exists('assets/videos_rerendered'):
    os.makedirs('assets/videos_rerendered')

# Function to convert videos using MoviePy
def convert_videos(df):
    print("Converting videos...")
    for idx, row in df.iterrows():
        input_path = os.path.join('assets', row['videoname'])
        output_path = os.path.join('assets/videos_rerendered', row['videoname'])
        
        # Skip if output already exists
        if os.path.exists(output_path):
            continue
            
        if os.path.exists(input_path):
            try:
                print(f"Converting: {row['videoname']}")
                video = VideoFileClip(input_path)
                video.write_videofile(output_path, codec='libx264', audio=False)
                video.close()
            except Exception as e:
                print(f"Error converting {row['videoname']}: {e}")

# Import and clean data
df = pd.read_csv('./assets/main.csv')

# Convert videos before starting the app
convert_videos(df)

# Add route to serve video files from videos_rerendered
@app.server.route('/videos/<path:path>')
def serve_video(path):
    """Serve video files from the videos_rerendered directory"""
    response = send_from_directory('assets/videos_rerendered', path)
    response.headers['Content-Type'] = 'video/mp4'
    return response

# App layout
app.layout = html.Div([
    html.H1("Multimodal Dynamic Data Visualizer", style={'text-align': 'center'}),
    
    html.Div(id='output_container', children=[], style={'color': 'white'}),
    html.Br(),
    
    dcc.Graph(
        id='MY_XY_Map', 
        figure={},
        style={'width': '49%', 'textAlign': 'center', 'display': 'inline-block'}
    ),
    
    html.Video(
        controls=True,
        id='videoplayer',
        src='',
        style={
            'width': '45%',
            'textAlign': 'center',
            'display': 'inline-block',
            'vertical-align': 'top'
        },
        autoPlay=True,
        muted=True,
        loop=True
    ),
    
    # Debug info display
    html.Div(id='debug-info', style={'margin-top': '20px', 'color': 'white'})
])

# Callback to update graph and video
@app.callback(
    [
        Output(component_id='output_container', component_property='children'),
        Output(component_id='MY_XY_Map', component_property='figure'),
        Output(component_id='videoplayer', component_property='src'),
        Output(component_id='debug-info', component_property='children')
    ],
    [Input('MY_XY_Map', 'clickData')]
)
def update_graph(clickData):
    container = "Click on any point to inspect the multimodal event associated with it."
    dff = df.copy()
    debug_info = ""

    # Create scatter plot
    fig = px.scatter(
        data_frame=dff,
        x='x',
        y='y',
        opacity=0.75,
        hover_data=['videoname'],
        template='plotly_dark'
    )
    
    # Adjust figure parameters
    fig.update_traces(marker_size=15)
    fig.update_layout(
        legend=dict(orientation="h"),
        xaxis_title="X Dimension",
        yaxis_title="Y Dimension"
    )
    fig['layout']['uirevision'] = 42
    
    # Handle video selection on click
    src = ''
    if clickData is not None:
        try:
            point_data = clickData['points'][0]
            video_name = point_data['customdata'][0]
            # Use the /videos route to serve the video
            src = f'/videos/{video_name}'
            
            # Add debug information
            debug_info = f"""
            Video name: {video_name}
            Video path: {src}
            Original exists: {os.path.exists(f'assets/{video_name}')}
            Converted exists: {os.path.exists(f'assets/videos_rerendered/{video_name}')}
            """
            print(f"Loading video: {src}")
            
        except Exception as e:
            debug_info = f"Error: {str(e)}"
            print(f"Error processing click data: {e}")
    
    return container, fig, src, debug_info

if __name__ == '__main__':
    # Print the contents of folders
    print("\nContents of original assets folder:")
    for file in os.listdir('assets'):
        print(f"- {file}")
    
    print("\nContents of rerendered videos folder:")
    if os.path.exists('assets/videos_rerendered'):
        for file in os.listdir('assets/videos_rerendered'):
            print(f"- {file}")
    
    app.run_server(debug=True)