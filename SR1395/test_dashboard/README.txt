install python (and vscode)
add pip to env path
set vscode interpreter to python installed
install chrome driver
pip install selenium
pip install pytest --html

For running single test:
run "pytest main.py -k test_3_PS2_overdue --html=TestReport.html --tb=short"
For running all tests:
run "pytest main.py --html=TestReport.html --tb=short"
