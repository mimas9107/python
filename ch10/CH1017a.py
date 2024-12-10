import sys

print('# of arguments:', len(sys.argv))

for i, v in enumerate(sys.argv):
    print('[', i, ']=', v)
    