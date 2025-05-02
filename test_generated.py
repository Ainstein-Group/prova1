Test unitari completi con pytest

```python
import pytest
from unittest.mock import patch
from labirinto import Labirinto
import logging

@pytest.fixture
def empty_grid():
    """Fixture for an empty grid."""
    return [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

@pytest.fixture
def default_grid():
    """Fixture for the default grid used in main."""
    return [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

@pytest.fixture
def same_start_goal_grid():
    """Fixture for grid where start and goal are the same."""
    return [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

def test_heuristic():
    """Test the heuristic method with various inputs."""
    lab = Labirinto([[0,0], [0,0]], (0,0), (0,0))
    assert lab.heuristic((0,0), (0,0)) == 0
    assert lab.heuristic((0,0), (1,1)) == 2
    assert lab.heuristic((2,3), (4,5)) == 4
    assert lab.heuristic((5,5), (2,3)) == 4

def test_astar_normal_case(default_grid):
    """Test A* algorithm with a normal case where path exists."""
    start = (0, 0)
    goal = (2, 2)
    lab = Labirinto(default_grid, start, goal)
    path = lab.astar()
    assert path is not None
    assert path[0] == goal

def test_astar_no_path(empty_grid):
    """Test A* algorithm when no path exists."""
    # Block all paths
    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    start = (0, 0)
    goal = (2, 2)
    lab = Labirinto(grid, start, goal)
    path = lab.astar()
    assert path == "Nessun percorso possibile"

def test_astar_start_equals_goal(same_start_goal_grid):
    """Test A* when start equals goal."""
    start = (1, 1)
    goal = (1, 1)
    lab = Labirinto(same_start_goal_grid, start, goal)
    path = lab.astar()
    assert path == [start]

def test_str_method(default_grid):
    """Test the __str__ method returns the grid as string."""
    lab = Labirinto(default_grid, (0,0), (0,0))
    str_repr = str(lab)
    assert str_repr == str(default_grid)

def test_main_function(default_grid):
    """Test the main function calls A* correctly."""
    with patch('labirinto.Labirinto') as mock_lab:
        instance = mock_lab.return_value
        instance.astar.return_value = [(2,2)]
        
        main()
        
        instance.astar.assert_called_once()

def test_logging_info(main_function):
    """Test logging.info is called with correct messages."""
    with patch('logging.info') as mock_logging:
        main()
        mock_logging.assert_called_with("Percorso trovato: %s", [(2, 2)])

def test_logging_start(main_function):
    """Test logging.info is called when search starts."""
    with patch('logging.info') as mock_logging:
        main()
        mock_logging.assert_called_with("Inizia ricerca percorso...")

def test_heuristic_edge_cases():
    """Test heuristic with edge cases."""
    lab = Labirinto([[0,0], [0,0]], (0,0), (0,0))
    assert lab.heuristic((0,0), (0,0)) == 0
    assert lab.heuristic((0,0), (10,10)) == 20
    assert lab.heuristic((-1,-1), (1,1)) == 4
```