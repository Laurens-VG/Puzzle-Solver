import numpy as np
from scipy.signal import square
import simpleaudio as sa
import re


def Audio(sample, rate):
    # Ensure that highest value is in 16-bit range
    audio = sample / np.max(np.abs(sample))
    audio = audio * (2 ** 15 - 1)
    # Convert to 16-bit data
    audio = audio.astype(np.int16)
    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, rate)
    # Wait for playback to finish before exiting
    play_obj.wait_done()


def freq_per_noot(noot, octaaf):
    if noot == 'p':
        return 0
    freq = 261.626 * 2 ** (
    (["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"].index(noot) / 12. + octaaf - 4))
    return freq


def play_music(melo, bpm, oct):
    fs = 44100
    basis_octaaf = oct
    basis_loopduur = 60 * 4 / bpm
    envelope_duration = 1 / (8 * 60 * bpm)
    samples = []
    t = np.linspace(0, 1, num=fs)  # error weg bij fs*4?
    envelope = 1 - np.exp(-5 * t / envelope_duration)
    wavetable = square(np.sin(2 * np.pi * t))
    for j in range(len(melo)):
        note = melo[j]
        duration_pattern = re.compile("^[0-9]{1,2}")
        pitch_pattern = re.compile("[a-zA-Z]#*")
        octave_pattern = re.compile("[0-9]$")
        special_pattern = re.compile("[.]")
        duration = duration_pattern.findall(note)
        pitch = pitch_pattern.findall(note)[0].lower()
        octave = octave_pattern.findall(note)
        special_duration = special_pattern.findall(note)
        if len(duration) == 0:
            duur = basis_loopduur / 4
        else:
            duur = basis_loopduur / int(duration[0])
        noot = pitch
        if len(octave) == 0:
            octaaf = basis_octaaf
        else:
            octaaf = int(octave[0])
        if len(special_duration) == 1:
            duur = duur * 1.5
        freq = freq_per_noot(noot, octaaf)
        for i in range(int(duur * fs)):
            samples.append(wavetable[int(i * freq % len(wavetable))] * envelope[i])
    Audio(samples, rate=fs)

