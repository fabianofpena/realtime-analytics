from pyflink.table import EnvironmentSettings, TableEnvironment

def create_table_env():
    env_settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
    table_env = TableEnvironment.create(env_settings)
    table_env.get_config().get_configuration().set_string('table.exec.source.idle-timeout', '1s')
    table_env.get_config().get_configuration().set_string('table.local-time-zone', 'UTC')
    return table_env
