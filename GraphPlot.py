import matplotlib.pyplot as plt

class GraphPlot:

    def __init__(self,img_count=[],rub_y=[],sdes_y=[],hc_y=[]):
        #self.title("abcd")
        self.img_count=img_count
        self.rub_y=rub_y
        self.sdes_y = sdes_y
        self.hc_y=hc_y


        fig = plt.figure()
        fig.canvas.set_window_title('Perceptual')

        # plotting the line 1 points
        plt.plot(img_count, rub_y, label="Rubik Algorithm")

        # line 2 points

        # plotting the line 2 points
        plt.plot(img_count, sdes_y, label="SDES Algorithm")

        # line 3 points

        # plotting the line 3 points

        plt.plot(img_count, hc_y, label="HC Algorithm")

        # naming the x axis
        plt.xlabel('Image Number')
        # naming the y axis
        plt.ylabel('PEID Security Level Value')
        # giving a title to my graph
        plt.title('Three Lines Showing Three Algorithms!')


        # show a legend on the plot
        plt.legend()


        # function to show the plot
        plt.grid(True)
        plt.show()

"""count_x = [1, 2, 3, 4,5]
rub_y = [2, 4, 1,5,1]
#x2 = [1, 2, 3,4,5]
sdes_y = [4, 1, 3.6,4,3]
#x3 = [1, 2, 3,4,5]
hc_y = [3, 2, 4,6,4]

cp=GraphPlot(count_x,rub_y,sdes_y,hc_y)"""