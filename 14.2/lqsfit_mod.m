% lqsfit_mod.m
% Este programa ajusta uma reta de mínimos quadrados aos dados do arquivo input1.dat

% Define variáveis:
% x, y − Vetores com os dados
% slope − Inclinação da reta ajustada
% y_int − Intercepto da reta ajustada

disp('Este programa ajusta uma reta de mínimos quadrados aos dados do arquivo input1.dat');

% Leitura do ficheiro
data = load('input1.dat');
x = data(:, 1);
y = data(:, 2);
n_points = length(x);

% Acumular estatísticas
sum_x = sum(x);
sum_y = sum(y);
sum_x2 = sum(x.^2);
sum_xy = sum(x .* y);

% Calcular médias
x_bar = sum_x / n_points;
y_bar = sum_y / n_points;

% Calcular coeficientes da regressão linear
slope = (sum_xy - sum_x * y_bar) / (sum_x2 - sum_x * x_bar);
y_int = y_bar - slope * x_bar;

% Exibir os coeficientes
disp('Regression coefficients for the least−squares line:');
fprintf(' Slope (m) = %8.3f\n', slope);
fprintf(' Intercept (b) = %8.3f\n', y_int);
fprintf(' No. of points = %8d\n', n_points);

% Plotar os dados e a reta ajustada
plot(x, y, 'bo');    % Pontos azuis
hold on;
xmin = min(x);
xmax = max(x);
ymin = slope * xmin + y_int;
ymax = slope * xmax + y_int;
plot([xmin xmax], [ymin ymax], 'r-', 'LineWidth', 2); % Reta ajustada
hold off;

% Títulos e legendas
title('\bfLeast−Squares Fit');
xlabel('\bf\itx');
ylabel('\bf\ity');
legend('Input data', 'Fitted line');
grid on;
