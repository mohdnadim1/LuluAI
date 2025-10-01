# luluai/plugins/manager.py

class PluginManager:
    """
    A manager for discovering, registering, and running plugins.
    """

    def __init__(self):
        self._plugins = {}

    def register_plugin(self, name, plugin_instance):
        """
        Registers a plugin instance with the given name.
        """
        if name in self._plugins:
            raise ValueError(f"Plugin with name '{name}' is already registered.")
        self._plugins[name] = plugin_instance
        print(f"Plugin '{name}' registered.")

    def run_plugin(self, name, input_text):
        """
        Runs a registered plugin with the given input.
        """
        if name not in self._plugins:
            raise ValueError(f"No plugin with name '{name}' is registered.")

        plugin = self._plugins[name]

        # Ensure the plugin has a 'process' method
        if not hasattr(plugin, 'process') or not callable(plugin.process):
            raise TypeError(f"Plugin '{name}' does not have a callable 'process' method.")

        return plugin.process(input_text)

    def list_plugins(self):
        """
        Returns a list of registered plugin names.
        """
        return list(self._plugins.keys())