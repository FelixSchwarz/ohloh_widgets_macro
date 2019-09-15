
This is an archived repository: I do not use this code anymore and I won't spend time on development/maintenance. Maybe code from this repo will be useful to someone - feel free to copy what you need (MIT license).

---

# Ohloh Widgets Macro

[Ohloh](http://www.ohloh.net) has some nice [widgets](https://www.ohloh.net/p/ohloh_widgets_macro/widgets) which you can put on your site to show some statistics about your project. This software is about a [Trac](https://trac.edgewall.org/) macro to make embedding these widgets in your trac wiki easy and does not force you to lower trac's security settings. Also this macro has a special API so you can modify any Ohloh widget so it blends in better with your layout.

The whole code is licensed under the very liberal [MIT license](http://en.wikipedia.org/wiki/MIT_License) so you can use it in your own code without problems.

## Usage

Display a single widget by specifying your project id and the widget name (the Javascript file name without the '.js' suffix):
```
[[OhlohWidget(483602, project_basic_stats)]]
```

Also you can display a group of widgets together:
```
[[OhlohWidgetGroup(483602, project_basic_stats, project_factoids, project_users?style=green)]]
```
This has the advantage that all widgets are grouped in a div so you can style it easily. For example the widget list on the left side of this page is a widget group with some custom 

### Configuration
Enable the macro in your trac.ini:
```
[components]
ohloh_widgets.macro = enabled
# if you want to have better display of certain macros, enable also widget modificators:
ohloh_widgets.* = enabled
```

### Dependencies and Compatibility
- Python 2.3-2.6
- [pycerberus](https://github.com/FelixSchwarz/pycerberus)
- Trac 0.11 or 0.12

### Customizing Widgets

Some [Ohloh widgets](https://www.ohloh.net/p/ohloh_widgets_macro/widgets) do not look nice on a trac page because some elements do not respect trac's layout (e.g. they use different colors for links). This macro already ships some modifiers which can change the appearance of some Ohloh macros with Javascript (jQuery) and CSS but you can easily add your own by writing a small plugin which implements this interface:
```python
# This class is in ohloh_widgets.api
class IOhlohWidgetModifier(Interface):
    def widget_name(self):
        """Return the name of the widget which this modifier can modify.
        
        The widget name is the name of the JS file (e.g. 'project_factoids.js')
        without the '.js' suffix (=> 'project_factoids').
        """
    
    def widget_fix(self):
        """Return a Genshi tag which is inserted directly after the widget's script 
        tag. Use this to add custom CSS/Javascript which whips the widget into shape
        (again)."""
```

