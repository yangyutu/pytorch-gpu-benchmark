My 3090 testing results

Key highlights:
 - Using double can be drastically slower


Raw results
benchmark start : 2023/02/16 20:40:38
Number of GPUs on current device : 1
CUDA Version : 11.3
Cudnn Version : 8200
Device Name : NVIDIA GeForce RTX 3090
uname_result(system='Linux', node='Yuguang-3090', release='5.15.79.1-microsoft-standard-WSL2', version='#1 SMP Wed Nov 23 01:01:46 UTC 2022', machine='x86_64')
                     scpufreq(current=3187.2010000000005, min=0.0, max=0.0)
                    cpu_count: 24
                    memory_available: 93701804032
Benchmarking Training float precision type resnet101 
resnet101 model average train time : 61.533451080322266ms
Benchmarking Training float precision type resnet152 
resnet152 model average train time : 89.08412456512451ms
Benchmarking Training float precision type resnet18 
resnet18 model average train time : 13.53416919708252ms
Benchmarking Training float precision type resnet34 
resnet34 model average train time : 22.202816009521484ms
Benchmarking Training float precision type resnet50 
resnet50 model average train time : 36.555819511413574ms
Benchmarking Training float precision type wide_resnet101_2 
wide_resnet101_2 model average train time : 104.43112850189209ms
Benchmarking Training float precision type wide_resnet50_2 
wide_resnet50_2 model average train time : 60.32169818878174ms
Benchmarking Inference float precision type resnet101 
resnet101 model average inference time : 20.170626640319824ms
Benchmarking Inference float precision type resnet152 
resnet152 model average inference time : 28.162760734558105ms
Benchmarking Inference float precision type resnet18 
resnet18 model average inference time : 4.826536178588867ms
Benchmarking Inference float precision type resnet34 
resnet34 model average inference time : 7.171716690063477ms
Benchmarking Inference float precision type resnet50 
resnet50 model average inference time : 11.863141059875488ms
Benchmarking Inference float precision type wide_resnet101_2 
wide_resnet101_2 model average inference time : 33.93202304840088ms
Benchmarking Inference float precision type wide_resnet50_2 
wide_resnet50_2 model average inference time : 19.286251068115234ms
Benchmarking Training half precision type resnet101 
resnet101 model average train time : 47.023491859436035ms
Benchmarking Training half precision type resnet152 
resnet152 model average train time : 68.45534801483154ms
Benchmarking Training half precision type resnet18 
resnet18 model average train time : 12.425975799560547ms
Benchmarking Training half precision type resnet34 
resnet34 model average train time : 18.57076644897461ms
Benchmarking Training half precision type resnet50 
resnet50 model average train time : 27.51584529876709ms
Benchmarking Training half precision type wide_resnet101_2 
wide_resnet101_2 model average train time : 66.34252548217773ms
Benchmarking Training half precision type wide_resnet50_2 
wide_resnet50_2 model average train time : 37.91157245635986ms
Benchmarking Inference half precision type resnet101 
resnet101 model average inference time : 15.880179405212402ms
Benchmarking Inference half precision type resnet152 
resnet152 model average inference time : 20.772075653076172ms
Benchmarking Inference half precision type resnet18 
resnet18 model average inference time : 4.8587751388549805ms
Benchmarking Inference half precision type resnet34 
resnet34 model average inference time : 6.676993370056152ms
Benchmarking Inference half precision type resnet50 
resnet50 model average inference time : 8.540549278259277ms
Benchmarking Inference half precision type wide_resnet101_2 
wide_resnet101_2 model average inference time : 19.263086318969727ms
Benchmarking Inference half precision type wide_resnet50_2 
wide_resnet50_2 model average inference time : 11.1273193359375ms
Benchmarking Training double precision type resnet101 
resnet101 model average train time : 1277.1468544006348ms
Benchmarking Training double precision type resnet152 
resnet152 model average train time : 1917.5536012649536ms
Benchmarking Training double precision type resnet18 
resnet18 model average train time : 298.89214038848877ms
Benchmarking Training double precision type resnet34 
resnet34 model average train time : 602.1729707717896ms
Benchmarking Training double precision type resnet50 
resnet50 model average train time : 670.0362205505371ms
Benchmarking Training double precision type wide_resnet101_2 
wide_resnet101_2 model average train time : 3189.181604385376ms
Benchmarking Training double precision type wide_resnet50_2 
wide_resnet50_2 model average train time : 1617.4304151535034ms
Benchmarking Inference double precision type resnet101 
resnet101 model average inference time : 387.8390169143677ms
Benchmarking Inference double precision type resnet152 
resnet152 model average inference time : 555.9559345245361ms
Benchmarking Inference double precision type resnet18 
resnet18 model average inference time : 108.68607521057129ms
Benchmarking Inference double precision type resnet34 
resnet34 model average inference time : 201.15576267242432ms
Benchmarking Inference double precision type resnet50 
resnet50 model average inference time : 215.59405326843262ms
Benchmarking Inference double precision type wide_resnet101_2 
wide_resnet101_2 model average inference time : 1024.5832920074463ms
Benchmarking Inference double precision type wide_resnet50_2 
wide_resnet50_2 model average inference time : 515.382285118103ms
benchmark end : 2023/02/16 20:53:50
end