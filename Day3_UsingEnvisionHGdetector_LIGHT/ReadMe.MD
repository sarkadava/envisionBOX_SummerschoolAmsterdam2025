# Installation in a conda environment
conda create -n envisionsumschool python=3.9
conda activate envisionsumschool
cd youfolder/Day3_UsingEnvisionHGdetector_LIGHT
pip install -r requirements.txt

# if not work try
install Visual C++ Redistributable https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170
conda create -n envisionsumschool python=3.9
conda activate envisionsumschool
pip cache purge
pip install -r requirements.txt