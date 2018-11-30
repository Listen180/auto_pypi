# 
# *********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2018-11-21 18:29
# * Last modified : 2018-11-30 15:09
# * Filename      : setup_new_pypi.sh
# * Description   : 
# *********************************************************


## Check on package name input
if [ "$1" == "" ]; then
    echo "parameter 1 missing: package name needed! "
    exit
fi



dist_folder="dist/"
build_folder="build/"
egg_info_folder="$1.egg-info/"

if [ -d $dist_folder ]; then
    echo "  removing old dist folder ... "
    rm -r $dist_folder
else
    echo "  dist folder not found. "
fi

if [ -d $build_folder ]; then
    echo "  removing old build folder ... "
    rm -r $build_folder
else
    echo "  build folder not found. "
fi

if [ -d $egg_info_folder ]; then
    echo "  removing old egg info folder ... "
    rm -r $egg_info_folder
else
    echo "  egg info folder not found. "
fi



## Prepare for uploading
python3 -m pip install --user --upgrade setuptools wheel
echo """
"""
python3 setup.py sdist bdist_wheel
echo """
"""

## Uploading check
python3 -m pip install --user --upgrade twine

echo """

Checking on the sdist and wheel ... (also check README rendering problem)
"""
twine check dist/*


## Upload
echo """
"""
while true; do
    read -p "Use Test PyPi? [Y/n]: (type 'n' to abort uploading procedure)" check_test
    case $check_test in
	[Yy]* ) twine upload --repository-url https://test.pypi.org/legacy/ dist/*; break;;
	#[Nn]* ) twine upload --repository-url https://upload.pypi.org/legacy/ dist/*; break;;
	[Nn]* ) exit; break;;
	* ) echo "Please answer yes or no.";;
    esac
done
