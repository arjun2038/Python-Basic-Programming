class DataHiding:
    __count=0

    def count(self):
        self.__count+=1
        print(self.__count)
data_hiding=DataHiding()
data_hiding.count()
data_hiding.count()
data_hiding.count()

