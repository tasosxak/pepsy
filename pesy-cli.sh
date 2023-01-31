echo 'git+https://github.com/tasosxak/pepsy.git' >> requirements.txt
echo 'brython==3.8.7' >> requirements.txt
pip install -r requirements.txt
python -m brython --update
python -m brython --add_package pepsy
echo 'Finished!'