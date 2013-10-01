python game_of_life/test/test_pixel.py
python game_of_life/test/test_universe.py

pylint --output-format=parseable game_of_life/*.py | tee pylint_out.txt
pep8 game_of_life/*.py | tee pep8_out.txt
clonedigger --cpd-output game_of_life/*.py -o clonedigger_out.xml
sloccount --duplicates --wide --details game_of_life/ > sloccount_out.txt
pymetrics game_of_life/*.py > complexity.txt
pycabehtml -i complexity.txt -o complexity.html -a complexity_acc.txt -g output.png
pyreverse -A -S -o png -p GameOfLife game_of_life/*.py

coverage run game_of_life/test/test_pixel.py
coverage run -a --omit=*mock* game_of_life/test/test_universe.py
coverage xml

doxygen Doxyfile
