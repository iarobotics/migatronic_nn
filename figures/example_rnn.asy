size(0,30cm);
import graph;

int dx = 4, dy = 6;

defaultpen(fontsize(25pt));


pen redPen = defaultpen + heavyred + 2*linewidth(defaultpen),
    bluePen = defaultpen + heavyblue + 2*linewidth(defaultpen),
    blackpen = defaultpen + 2*linewidth(defaultpen),
    greenPen = defaultpen + deepgreen + 2*linewidth(defaultpen);


draw(Circle((dx,dy), 2), redPen);

label("$z_0 =$", (dx, dy), align=NoAlign, p=redPen);
label("$x_0 \cdot w_0 + b_0$", (dx, dy-0.5), align=NoAlign, redPen);

draw((dx,0)--(dx,dy-2), Arrow);
draw((dx,0)--(dx,dy-2), blackpen);
label("$w_0$", (dx, dy-4), align=E, blackpen);
label("$x_0$", (dx, 0), align=E, blackpen);

draw((0,dy-4)--(dx,dy-2), Arrow);
draw((0,dy-4)--(dx,dy-2), blackpen);



draw(Circle((3*dx,dy), 5), bluePen);


label("\textbf{Hidden layer}", (2*dx, 3*dy + 1), N, bluePen);
label("\textbf{Output}", (3*dx, 2.5*dy + 1.5), N, greenPen);

draw((0,-1.5)--(4*dx -2, 3*dy + 2), invisible);
