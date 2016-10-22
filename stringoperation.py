str = 'X-DSPAM-Confidence: 0.8475'
start = str.find(':') + 2
print(float(str[start:]))