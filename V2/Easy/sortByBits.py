def sortByBits(arr):
        bit_holder = {0 : []}
        result = []
        for i in arr:
            temp = '{0:08b}'.format(i)
            if (temp.count('1') in bit_holder):
                bit_holder[temp.count('1')].append(i)
            else:
                bit_holder[temp.count('1')] = []
                bit_holder[temp.count('1')].append(i)
        for j in sorted(bit_holder):
            result.extend(sorted(bit_holder[j]))
        return result


sortByBits([1024,512,256,128,64,32,16,8,4,2,1])