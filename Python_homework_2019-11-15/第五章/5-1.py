def demo(*para):#接收任意实数，返回一个元组，第一个元素为平均值，其他为大于平均数的实数
    avg=sum(para)/len(para)
    g=[i for i in para if i>avg]
    return (avg,)+tuple(g)