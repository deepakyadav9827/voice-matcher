import librosa
import numpy as np
from scipy.spatial.distance import cosine

def extract_features(audio_path):
    y, sr = librosa.load(audio_path)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs.T, axis=0)

def compare_voices(path1, path2, threshold=0.6):
    f1 = extract_features(path1)
    f2 = extract_features(path2)
    similarity = 1 - cosine(f1, f2)
    print("Voice Similarity Score:", similarity)
    return similarity >= threshold
