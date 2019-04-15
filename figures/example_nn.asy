size(0,20cm);
import graph;
//import fontsize;

int dx = 4, dy = 3;

defaultpen(fontsize(20pt));

void interSphere(pair[] c1, pair[] c2) {
    pen whitepen = defaultpen + white + 4*linewidth(defaultpen);
    for(int i = 0; i < c1.length; ++i) {
        for(int j = 0; j < c2.length; ++j) {
            pair delta = 1.1*unit(c2[j]-c1[i]);
            draw(c1[i]+delta--c2[j]-delta, whitepen);
            draw(c1[i]+delta--c2[j]-delta, Arrow);
        }
    }
}

void unitCircs(pair[] c0, pen p = defaultpen) {
    for(int i = 0; i < c0.length; ++i) {
        draw(Circle(c0[i], 1), p);
    }
}

pair[] c0 = {(dx, 0.5dy), (dx, 1.5*dy), (dx, 2.5*dy)},
       c1 = {(2*dx, 0), (2*dx, dy), (2*dx, 2*dy), (2*dx, 3*dy)},
       c2 = {(3*dx, dy), (3*dx, 2*dy)};

pen redPen = defaultpen + heavyred + 2*linewidth(defaultpen),
    bluePen = defaultpen + heavyblue + 2*linewidth(defaultpen),
    greenPen = defaultpen + deepgreen + 2*linewidth(defaultpen);

unitCircs(c0, redPen); unitCircs(c1, bluePen); unitCircs(c2, greenPen);

interSphere(c0, c1);
interSphere(c1, c2);


label("\textbf{Input}", (dx, 2.5*dy + 1.5), N, redPen);
label("\textbf{Hidden layer}", (2*dx, 3*dy + 1), N, bluePen);
label("\textbf{Output}", (3*dx, 2.5*dy + 1.5), N, greenPen);

draw((dx-2,-1.5)--(4*dx -2, 3*dy + 2), invisible);

