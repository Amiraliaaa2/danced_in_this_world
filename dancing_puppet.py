#    @Amiraliaaa2
#    instagram : @amirali.aaa_

import tkinter as tk

class DancingFigure:
    def __init__(self, root):
        self.root = root
        self.root.title("رقصيديم در جهان تنگ بنا شده ، اين ارواح  مغروق مردگان رها شده")
        
        self.canvas = tk.Canvas(root, width=500, height=500, bg='black')  
        self.canvas.pack()
        
        # Initialize figure parts
        self.head = self.canvas.create_oval(220, 100, 280, 160, fill='white')  
        self.left_eye = self.canvas.create_oval(235, 120, 245, 130, fill='black')  
        self.right_eye = self.canvas.create_oval(255, 120, 265, 130, fill='black') 
        self.mouth = self.canvas.create_line(240, 145, 260, 145, width=2, fill='red')  
        self.body = self.canvas.create_line(250, 160, 250, 300, width=3, fill='white')  
        self.left_arm = self.canvas.create_line(250, 200, 200, 250, width=3, fill='white')  
        self.right_arm = self.canvas.create_line(250, 200, 300, 250, width=3, fill='white')  
        self.left_hand = self.canvas.create_oval(190, 240, 210, 260, fill='white')  
        self.right_hand = self.canvas.create_oval(290, 240, 310, 260, fill='white')  
        self.left_leg = self.canvas.create_line(250, 300, 200, 400, width=3, fill='white')  
        self.right_leg = self.canvas.create_line(250, 300, 300, 400, width=3, fill='white')  
        self.left_foot = self.canvas.create_oval(190, 390, 210, 410, fill='white')  
        self.right_foot = self.canvas.create_oval(290, 390, 310, 410, fill='white')  

        self.animation_step = 0
        self.animate()

    def animate(self):
        if self.animation_step == 0:
            self.canvas.coords(self.left_arm, 250, 200, 180, 230)  
            self.canvas.coords(self.right_arm, 250, 200, 320, 230) 
            self.canvas.coords(self.left_hand, 170, 220, 190, 240) 
            self.canvas.coords(self.right_hand, 310, 220, 330, 240)
            self.canvas.coords(self.left_leg, 250, 300, 220, 420)  
            self.canvas.coords(self.right_leg, 250, 300, 280, 420) 
            self.canvas.coords(self.left_foot, 210, 410, 230, 430) 
            self.canvas.coords(self.right_foot, 270, 410, 290, 430)
            self.canvas.coords(self.mouth, 240, 145, 260, 145)  # simple smile
        elif self.animation_step == 1:
            self.canvas.coords(self.left_arm, 250, 200, 200, 250)  
            self.canvas.coords(self.right_arm, 250, 200, 300, 250) 
            self.canvas.coords(self.left_hand, 190, 240, 210, 260) 
            self.canvas.coords(self.right_hand, 290, 240, 310, 260)
            self.canvas.coords(self.left_leg, 250, 300, 200, 400)  
            self.canvas.coords(self.right_leg, 250, 300, 300, 400) 
            self.canvas.coords(self.left_foot, 190, 390, 210, 410) 
            self.canvas.coords(self.right_foot, 290, 390, 310, 410)
            self.canvas.coords(self.mouth, 240, 145, 260, 145)  # simple smile
        elif self.animation_step == 2:
            self.canvas.coords(self.left_arm, 250, 200, 200, 230)  
            self.canvas.coords(self.right_arm, 250, 200, 300, 230) 
            self.canvas.coords(self.left_hand, 190, 220, 210, 240) 
            self.canvas.coords(self.right_hand, 290, 220, 310, 240)
            self.canvas.coords(self.left_leg, 250, 300, 180, 420)  
            self.canvas.coords(self.right_leg, 250, 300, 320, 420) 
            self.canvas.coords(self.left_foot, 170, 410, 190, 430) 
            self.canvas.coords(self.right_foot, 330, 410, 350, 430)
            self.canvas.coords(self.mouth, 240, 145, 260, 145)  # simple smile
        elif self.animation_step == 3:
            self.canvas.coords(self.left_arm, 250, 200, 200, 270)  
            self.canvas.coords(self.right_arm, 250, 200, 300, 270) 
            self.canvas.coords(self.left_hand, 190, 260, 210, 280) 
            self.canvas.coords(self.right_hand, 290, 260, 310, 280)
            self.canvas.coords(self.left_leg, 250, 300, 220, 400)  
            self.canvas.coords(self.right_leg, 250, 300, 280, 400) 
            self.canvas.coords(self.left_foot, 210, 390, 230, 410) 
            self.canvas.coords(self.right_foot, 270, 390, 290, 410)
            self.canvas.coords(self.mouth, 240, 145, 260, 145)  # simple smile

        self.animation_step = (self.animation_step + 1) % 4
        self.root.after(300, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = DancingFigure(root)
    root.mainloop()
