# spectre
Create audio files with hidden spectral messages. Just type the text to be displayed, name the output audio file and run the program. 
Play the audio file, and run any spectrogram app on your smartphone or tablet. Watch the hidden message appear on the screen.
Example output attached - audio and screenshoot. 

Input:

disp - text to be displayed

foutname - name of the output audio file

flow - lowest frequency (bottom symbol dot line) [Hz]

df - step size between subsequent dots in frequency domain [Hz]

tdot - duration time of a single column [s]

nfreqs - number of rows, do not change unless you also use different symbol codes

fs - sampling frequency of the output audio file [Hz]


Output:

.wav file created in the current directory

List of the available symbols can be found in the symbols5x8.py

The output audio file can be also mixed with any other sound, just try to keep the frequency contents separated.
