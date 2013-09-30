cd game_of_life
python test_pixel.py
python test_universe.py

pyreverse -A -S -o png -p GameOfLife *.py
pylint --output-format=parseable *.py | tee pylint_out.txt

pep8 *.py | tee pep8_out.txt

clonedigger --cpd-output *.py -o clonedigger_out.xml

sloccount --duplicates --wide --details . > sloccount_out.txt

pymetrics *.py > complexity.txt
pycabehtml -i complexity.txt -o complexity.html -a complexity_acc.txt -g output.png

cd ..

coverage run game_of_life/test_pixel.py
coverage run -a game_of_life/test_universe.py
coverage xml

doxygen Doxyfile
