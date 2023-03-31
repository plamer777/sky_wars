"""This file contains OptionsView class to display options pages"""
import os
from flask import Blueprint, request, render_template
from werkzeug.utils import secure_filename
from constants import AVATAR_DIR
from services.equipment_service import EquipmentService
from services.phrases_service import PhrasesService
from services.unit_class_service import UnitClassService
from services.skills_service import SkillsService
from container import auth_service
# ------------------------------------------------------------------------
options_blueprint = Blueprint('options_blueprint', __name__)
# ------------------------------------------------------------------------


class OptionsView:
    """The OptionsView class provides methods to display main options page
    and another pages"""
    @staticmethod
    @options_blueprint.route('/options/')
    @auth_service.check_rules
    def options_page() -> str:
        """This method serves to display options page
        :return: An html template
        """
        return render_template('choose_option.html')

    @staticmethod
    @options_blueprint.route('/add-weapon/', methods=['POST', 'GET'])
    @auth_service.check_rules
    def add_weapon_page() -> str:
        """This method serves to display add-weapon page and get data from
        user to add
        :return: An html template
        """
        if request.method == 'GET':
            return render_template('add_weapon.html')

        else:
            weapon_data = request.form
            result = EquipmentService().add_weapon(weapon_data)
            return render_template('add_weapon.html', result=result)

    @staticmethod
    @options_blueprint.route('/add-armor/', methods=['POST', 'GET'])
    @auth_service.check_rules
    def add_armor_page() -> str:
        """This method serves to display add-armor page and get data from
        user to add
        :return: An html template
        """
        if request.method == 'GET':
            return render_template('add_armor.html')

        else:
            armor_data = request.form
            result = EquipmentService().add_armor(armor_data)
            return render_template('add_armor.html', result=result)

    @staticmethod
    @options_blueprint.route('/add-class/', methods=['POST', 'GET'])
    @auth_service.check_rules
    def add_class_page() -> str:
        """This method serves to display add-class page and get data from
        user to add
        :return: An html template
        """
        if request.method == 'GET':
            return render_template('add_class.html')

        else:
            class_data = dict(request.form)
            avatar = request.files.get('avatar')

            if avatar:
                filename = secure_filename(avatar.filename)
                avatar.save(os.path.join(AVATAR_DIR, filename))
                class_data['avatar'] = filename
                result = UnitClassService().add_new(class_data)
            else:
                result = 'Avatar is required, try again'

            return render_template('add_class.html', result=result)

    @staticmethod
    @options_blueprint.route('/add-skill/', methods=['POST', 'GET'])
    @auth_service.check_rules
    def add_skill_page() -> str:
        """This method serves to display add-skill page and get data from
        user to add
        :return: An html template
        """
        if request.method == 'GET':
            return render_template('add_skill.html')

        else:
            skill_data = request.form
            result = SkillsService().add_new(skill_data)
            return render_template('add_skill.html', result=result)

    @staticmethod
    @options_blueprint.route('/add-logs/', methods=['POST', 'GET'])
    @auth_service.check_rules
    def add_logs_page() -> str:
        """This method serves to display add-logs page and get data from
        user to add
        :return: An html template
        """
        if request.method == 'GET':
            return render_template('add_logs.html')

        else:
            logs_data = request.form
            result = PhrasesService().add_new(*logs_data.values())
            return render_template('add_logs.html', result=result)
