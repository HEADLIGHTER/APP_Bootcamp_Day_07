## Voight-Kampf test

### Check if you are a human or a replicant

1. Run:

        python3 main.py
2. Questions and answers to them are displayed automatically.
3. After that, you need to enter the following parameters:

    - respiration
    - heart rate
    - blushing level
    - pupillary dilation

4.  Stopping test if the entered data does not pass 
5. Counting mean values

6. 6To create documentation, you need to install the 'Sphinx':

         python3 -m venv venv
         . venv/bin/activate
         pip install --upgrade pip
         pip install -U sphinx
8. Then, being in the 'docs' folder, you need to run the Makefile:
make html
9. After that, open _build/html/index.html