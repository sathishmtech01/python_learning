# create figure
import matplotlib.pyplot as plt

fig = plt.figure()
fig3 = plt.figure()
fig2 = plt.figure(figsize=plt.figaspect(2.0))

#fig.add_axes()
# 121 - split 1- row, 2 - column and 1- element
ax1 = fig.add_subplot(241)
ax2 = fig.add_subplot(142)
ax3 = fig.add_subplot(143)
ax4 = fig.add_subplot(245)
ax5 = fig3.add_subplot(346)

ax1.plot([1,2,3],[1,2,3])

#ax6 = fig.add_subplot(235)
#ax3 = fig.add_subplot(236)
# print("Hello")
# # row-col-num
# ax3 = fig.add_subplot(212)
fig3, axes = plt.subplots(nrows=2,ncols=2)
fig4, axes2 = plt.subplots(ncols=3)
plt.show()
