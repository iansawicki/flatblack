# Download conda
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh -O ~/miniforge3.sh 

# Install conda
bash ~/miniforge3.sh

# Add conda to path
echo "export PATH=$PATH:$HOME/miniforge3/bin" >> $HOME/.bash_profile
