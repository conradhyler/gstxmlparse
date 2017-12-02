import xml.etree.ElementTree as ET
import sys
path = sys.argv[1]
GST_file = open(path,'r')
GST_stats = GST_file.read()
tree = ET.parse(path)
root = tree.getroot()
new_path = sys.argv[2]
new_test = open(new_path,'a')
print ' '
print path
for elem in tree.iter(tag='DisplayScaleFrom'):
    dsf = elem.text
    print('DisplayScaleFrom: ' + str(dsf))
for elem in tree.iter(tag='DisplayScaleTo'):
    dst = elem.text
    print('DisplayScaleTo: ' + str(dst))
for elem in tree.iter(tag='LabelScaleTo'):
    lst = elem.text
    print('LabelScaleTo: ' + str(lst))
for elem in tree.iter(tag='LabelScaleFrom'):
    lsf = elem.text
    print('LabelcaleFrom: ' + str(lsf))
for elem in tree.iter(tag='Visible'):
    vis = elem.text
    print('Visible: ' + str(vis))
for elem in tree.iter(tag='DrawOnAerial'):
    doa = elem.text
    print('DrawOnAerial: ' + str(doa))
new_test.write('\n' + path + ', ' + str(dsf)+ ', '+str(dst) + ', ' + str(lsf)+ ', '+str(lst) + ', ' + str(vis)+ ', '+str(doa))
GST_file.close()
new_test.close()