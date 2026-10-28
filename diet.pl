
% Diet suggestions based on disease

diet(diabetes, 'Balanced meals with controlled carbohydrates').
diet(obesity, 'Portion-controlled meals with vegetables and fruits').
diet(anemia, 'Iron-rich foods such as beans and leafy vegetables').
diet(hypertension, 'Low-sodium foods and fresh vegetables').
diet(fever, 'Fluids and easily digestible foods').

% Rule to suggest diet
suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).
