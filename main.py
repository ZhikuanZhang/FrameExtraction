import config as cf
import function as f

#每60秒取3帧
def test_one():
        f.method_one(cf.DATA_PATH + 'test.mp4', cf.PATH1, 60, 3)
        return

#十等分，每部分取5帧
def test_two():
        f.method_two(cf.DATA_PATH + 'test.mp4', cf.PATH2, 10, 5)
        return

#每隔100帧取一次
def test_three():
        f.method_three(cf.DATA_PATH + 'test.mp4', cf.PATH3, 100)
        return

if __name__ == '__main__':
        test_one()
        #test_two()
        #test_three()