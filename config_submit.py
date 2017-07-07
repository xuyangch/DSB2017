config = {
            #'datapath':'/Volumes/Hyacinth/luna16/',
            'datapath':'/Users/hyacinth/Downloads/kaggle/stage2',
            'preprocess_result_path':'/Users/hyacinth/PycharmProjects/DSB2017-master/prep_result',
            'outputfile':'prediction.csv',
          
            'detector_model':'net_detector',
            'detector_param':'./model/detector.ckpt',
            'classifier_model':'net_classifier',
            'classifier_param':'./model/classifier.ckpt',
            #'n_gpu':8,
            'n_gpu':1,
            #'n_worker_preprocessing':None,
            'n_worker_preprocessing':1,
            'use_exsiting_preprocessing':True,
            'skip_preprocessing':True,
            'skip_detect':False,
            'use_mhd': False
        }
