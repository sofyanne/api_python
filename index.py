# coding: utf-8
import src.controller.recipe as recipe_controller
import src.fixtures.app as fixtures
import cgi

print("Content-type: application/json; charset=utf-8\n")
recipe_controller.index()
