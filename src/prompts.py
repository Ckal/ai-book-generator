def get_initial_prompts(
    key,
    type_of_main_character,
    main_character_name,
    skill_development,
    learning_objectives,
    theme,
    topic,
):

    prompts = {
        "Fairy tales": f"I am a land far far away there was a {type_of_main_character} who is famous by the name {main_character_name} . {main_character_name} always had a  good{skill_development} and the story revolves around {learning_objectives} ,once can learn about {theme}. This is a famous topic consisting of {topic} for childrens "
    }

    return prompts.get(key)


def story_setting_prompt(
    key,
    type_of_main_character,
    main_character_name,
    skill_development,
    learning_objectives,
    theme,
    mood_of_story,
    ant_name,
    ant_type,
):
    prompts = {
        "Fairy tales": f"{main_character_name} was always inclined towards {mood_of_story} but there was a {ant_type} famoulsy known as {ant_name} the {ant_type} who did not like {main_character_name}"
    }
    return prompts.get(key)


def supporting_character_inclusion(key, sup_name, sup_type, positive_messaging):
    prompts = {
        "Fairy tales": f"Our hero who was always a supporter of {positive_messaging} had an friend named {sup_name} who was a {sup_type}"
    }
    return prompts.get(key)


def ending_scene(key, resolution, main_char, positive_mess):
    prompts = {
        "Fairy tales": f"So this concludes that {main_char} was focused on getting {positive_mess} out for the world which resulted in {resolution}"
    }
    return prompts.get(key)
