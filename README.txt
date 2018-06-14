The images need to be in the same directory as the class and the script. To run the program enter the following:

    python3 FFT_Script.py <image.pgm> <task> 

Upon initialising an image it is shown uncorrected. After the user closes this window the correction process takes place and the corrected image is shown.

if <task> = '0': The program produces a plot of the autocorrelation between any 2 lines. At present the indices of the two lines are hardcoded into the script and user must manually change these to check different lines.

if <task> = ‘1’: Selected image is corrected by running the ‘Index_Engine’ method described in the BACKGROUND document.

if <task> = ‘2’: Selected image is corrected by running the ‘Shift_Engine’ method described in the BACKGROUND document.