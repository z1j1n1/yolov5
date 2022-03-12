from ruamel.yaml import YAML
import random

yaml = YAML()
with open("yolov5s.yaml", encoding='ascii', errors='ignore') as f:
    arch = yaml.load(f)

ConvChannels = [-1,128,256,512]
C3Channels = [128,256,512]
Strides = {'P3':8, 'P4':16, 'P5':32, 'P6':64, 'P7':128} #目前只在P3,P4,P5,确定Validation时为什么出现image_size=672可以考虑P6,P7
NConcat = 8

feature = [[3,'P3'],[5,'P4'],[9,'P5']]
Output = {'P3':3, 'P4':5, 'P5':9}
LayerCount = 10

Neck = []
for i in range(NConcat):
    x1,x2 = random.sample(feature,2)
    ConvChannel1 = random.sample(ConvChannels,1)[0]
    ConvChannel2 = random.sample(ConvChannels,1)[0]
    C3Channel = random.sample(C3Channels,1)[0]
    OutStride = random.sample(Strides.items(),1)[0]

    feature.append([LayerCount,OutStride[0]])
    if OutStride[0] in ['P3','P4','P5']:
        Output[OutStride[0]] = LayerCount
    Neck.append([[x1[0],x2[0]],1,'ConcatCell',[C3Channel,OutStride[1]/Strides[x2[1]],ConvChannel1,ConvChannel2]])
    print([x1[0],x2[0]],1,'ConcatCell',[C3Channel,OutStride[1]/Strides[x2[1]],ConvChannel1,ConvChannel2],OutStride[0])
    LayerCount += 1

Neck.append([list(Output.values()),1,'Detect',['nc', 'anchors']])
print([list(Output.values()),1,'Detect',['nc', 'anchors']])
arch['head'] = Neck

with open('yolov5s-NeckSearch-random-P7.yaml', "w") as f:
    yaml.default_flow_style = False
    yaml.dump(arch,f)




