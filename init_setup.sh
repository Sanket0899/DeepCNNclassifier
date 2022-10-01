
echo [$(date)]: "START"
echo [$(date)]: "Creating env with python 3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activating environment"
source activate ./env
echo [$(date)]: "installing dev requirement"
pip install -r requirements_dev.txt
echo [$(date)]: "END"