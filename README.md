# nnAudio2
Audio processing by using pytorch 1D convolution network (based on nnAudio)

# Install
```
$ pip install nnAudio2
```

# Dependencies
Numpy 1.14.5

Scipy 1.2.0

PyTorch 1.1.0

Python >= 3.6

librosa = 0.7.0 (Theortically nnAudio depends on librosa. But we only need to use a single function `mel` from `librosa.filters`. To save users troubles from installing librosa for this single function, I just copy the chunks of functions corresponding to `mel` in my code so that nnAudio runs without the need to install librosa)

# Quick Start
Gammatone Spectrogram is now available in nnAudio2, and other details can be found in https://github.com/KinWaiCheuk/nnAudio.
In addition, more audio augmentation methods are available in nnAudio2, according to https://github.com/qiuqiangkong/torchlibrosa.

### 1. STFT
```python
from nnAudio2 import Spectrogram
Spectrogram.STFT(n_fft=2048, freq_bins=None, hop_length=512, window='hann', freq_scale='no', center=True, pad_mode='reflect', fmin=50,fmax=6000, sr=22050, trainable=False)
```

### 2. Mel Spectrogram
```python
Spectrogram.MelSpectrogram(sr=22050, n_fft=2048, n_mels=128, hop_length=512, window='hann', center=True, pad_mode='reflect', htk=False, fmin=0.0, fmax=None, norm=1, trainable_mel=False, trainable_STFT=False)
```

### 3. CQT
```python
Spectrogram.CQT(sr=22050, hop_length=512, fmin=220, fmax=None, n_bins=84, bins_per_octave=12, norm=1, window='hann', center=True, pad_mode='reflect')
```

### 4. Gammatone Spectrogram
```python
Spectrogram.Gammatonegram(sr=44100, n_fft=2048, n_bins=64, hop_length=512, window='hann', center=True, pad_mode='reflect', htk=False, fmin=50.0, fmax=None, norm=1, trainable_bins=False, trainable_STFT=False)
```

#### The Gammatone filters by nnAudio2
![alt text](https://github.com/WangHelin1997/nnAudio2/blob/master/tips/gammatone.png)
