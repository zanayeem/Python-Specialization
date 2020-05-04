text = "X-DSPAM-Confidence:    0.8475";
pos=text.find('0')
text=text[pos:]
print (float(text))