from symbols5x8	import s5x8 as symbols   #5x8 symbols codes
from math import sin, cos, pi
import wave, array

#String to display on spectrogram:
disp='Hello world!'
#Output filename:
foutname='spectre.wav'

#some parameters:
flow=16000   #frequency of the lowest dot on spectrogram
df=250      #frequency steps between subsequent dots
tdot=0.25    #timespan of a single dot (column) on spectrogram
nfreqs=8    #number of frequencies - must be equal to the number of dots in single column in each sign
fs = 44100  #sampling frequency of output .wav file


#compute remaining parameters:
tdisp=len(disp)*5*tdot  #display time: number of symbols * 5 columns per symbol * display time of a single column
nsamples=tdisp*fs
freqs=list(range(flow,flow+(nfreqs-1)*df+1,df))
dt=1/fs
samplesperdot=int(tdot*fs)





#synthetize sound:
sound = array.array('h') # signed short integer (-32768 to 32767) array for sound samples
samplenr=0  #number of current sample
for zn in disp:
    for kl in symbols[zn]:
        freqflag='{0:08b}'.format(kl)   #flags for specific frequencies: format 0bxxxxxx
        for lczsmpl in range(samplesperdot):    #initiate and compute value of each sample:
            sample=0   
            for lcz in range(nfreqs):
                sample=sample + int(freqflag[lcz])*int(sin(2*pi*freqs[nfreqs-lcz-1]*samplenr*dt) * 32767/ nfreqs)    #normalization (max value of nrfreqs sine function combination is nrfreqs) and scaling to data full scale (integer max 32767)
            sound.append(int(sample))
            samplenr+=1     #increase sample number
    #space between subsequent symbols:
    for lczsmpl in range(samplesperdot):        
        sound.append(0)
        samplenr+=1
        
f = wave.open(foutname, 'w')
f.setparams((1, 2, fs, samplenr, "NONE", "Uncompressed"))
f.writeframes(sound.tostring())
f.close()
