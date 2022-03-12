path_to_images = '/content/drive/MyDrive/mask/dataset/'
path_to_backup = '/content/drive/MyDrive/mask/backup/'
path_to_training = '/content/drive/MyDrive/mask/training/'

# To count number of classes
cpt_classes = 0
print("Script start............")

with open(path_to_images + 'classes.names', 'w') as names, open(path_to_images + 'classes.txt', 'r') as txt:
    for line in txt:
        names.write(line)
        cpt_classes +=1

with open(path_to_training + 'labelled_data.data', 'w') as data:
    data.write('classes = ' + str(cpt_classes) + '\n') #write number of classes in the file
    data.write('train = ' + path_to_training + 'train.txt' + '\n') #path to train file
    data.write('valid = ' + path_to_training + 'test.txt' + '\n') #path to test file
    data.write('names = ' + path_to_images + 'classes.names' + '\n') #path to classes name file
    data.write('backup = ' + path_to_backup) #path to backup directory

print("Script end............")