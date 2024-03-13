import os

CURRENT_DIRECTORY = os.getcwd()
FILESTRUCTURE = {"rank0": ["libft"],
                 "rank1": ["get_nextline",
                           "ft_printf",
                           "born2beroot"],
                 "rank2": ["push_swap",
                           "minitalk",
                           "pipex",
                           "so_long",
                           "fdf",
                           "fract-ol"],
                 "rank3": ["minishell",
                           "philosophers"],
                 "rank4": ["cub3d",
                           "minirt",
                           "netpractice",
                           "cpp_module_00",
                           "cpp_module_01",
                           "cpp_module_02",
                           "cpp_module_03",
                           "cpp_module_04"],
                 "rank5": ["webserv",
                           "ft_irc",
                           "inception"
                           "cpp_module_05",
                           "cpp_module_06",
                           "cpp_module_07",
                           "cpp_module_08",
                           "cpp_module_09"],
                 "rank6": ["ft_transcendence"]}

def make_filestructure():
    parent_directory = "codam_core"
    parent_path = os.path.join(CURRENT_DIRECTORY, parent_directory)
    os.mkdir(parent_path)
    for rank_name, projects in FILESTRUCTURE.items():
        rank_path = os.path.join(parent_path, rank_name)
        os.mkdir(rank_path)
        for project_name in projects:
            project_path = os.path.join(rank_path, project_name)
            os.mkdir(project_path)
    
def main():
    make_filestructure()

main()