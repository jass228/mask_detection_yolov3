import os

path_to_images = '/content/drive/MyDrive/mask/dataset/'
path_to_training = '/content/drive/MyDrive/mask/training/'

os.chdir(path_to_images)

p = []
pct_test = 0.20 #percentage of test data

print("Script start............")

for current_dir, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.png'):
            path_to_save_into_txt_files = path_to_images + f
            p.append(path_to_save_into_txt_files + '\n')

p_test = p[:int(len(p) * pct_test)] #Slicing first percentage of elements from the list to write into the test.txt file
p = p[int(len(p) * pct_test):] #Deleting from initial list first percentage of elements

with open(path_to_training + 'train.txt', 'w') as train_txt:
    for elt in p:
        train_txt.write(elt)
        
with open(path_to_training + 'test.txt', 'w') as test_txt:
    for elt in p_test:
        test_txt.write(elt)

print("Script end............")