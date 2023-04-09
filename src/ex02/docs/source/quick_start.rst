Voight-Kampf test
==================
Check if you are a human or a replicant

Run
-----------------
0. python3 main.py


1. Questions and answers to them are displayed automatically.

2. After that, you need to enter the following parameters:
::

    - respiration
    - heart rate
    - blushing level
    - pupillary dilation

3. Stopping test if the entered data does not pass

4. Counting mean values and prints if test subject is human or replicant

5. To create documentation, you need to install the 'Sphinx':
::
    python3 -m venv venv
    source venv/bin/activate
    pip install sphinx

6. Then, being in the 'docs' folder, you need to run the Makefile:
::
    make html

7. After that open generated index.html file