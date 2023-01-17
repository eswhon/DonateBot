#    Donate Bot, A Simple Telegram Bot to tell How to Donate you
#    Copyright (C) 2021 Jayant Kageri
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os

ENV = os.environ.get("ENV")



class Var(object):
  if ENV:
    API_ID = int(os.environ.get('API_ID'))
    APP_HASH = os.environ.get('API_HASH')
    TOKEN = os.environ.get('TOKEN')
    OWNER_ID = int(os.environ.get('OWNER_ID'))
    DONATE_TEXT = os.environ.get('DONATE_TEXT')

  else:
    API_ID = "16209450"
    API_HASH = "a4573c55ebf7c23038b927997447b78d"
    TOKEN = "5674000763:AAFVqEQpOv-P6O2ty0-jrCmEgVXMzjru3Es"
    OWNER_ID = "2022313646"
    DONATE_TEXT = "Put your Donat Text/Message to be repeated here"
