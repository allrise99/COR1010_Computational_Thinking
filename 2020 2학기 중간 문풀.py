print("*문제1*")

temp = input("총 급여와 원천징수세율?")
total, tax = temp.split(", ")
total = int(total)
tax = float(tax)
m_tax = total * tax

print("원천징수세(%.3f%%):%.1f원"%(tax, m_tax))
