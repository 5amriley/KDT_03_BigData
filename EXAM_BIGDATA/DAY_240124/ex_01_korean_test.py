import matplotlib.pyplot as plt
import koreanize_matplotlib     # 한글을 사용할 수 있게 하는 라이브러리

plt.plot([-1, 0, 1, 2])
plt.title('그래프 제목', fontweight="bold")
plt.xlabel('간단한 그래프')
plt.show()
