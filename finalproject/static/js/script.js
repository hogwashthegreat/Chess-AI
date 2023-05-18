var config = {
  draggable: true,
  dropOffBoard: 'snapback', // this is the default
  position: 'start'
}
var board = Chessboard('board1', config)
$('#startBtn').on('click', board.start)
$('#clearBtn').on('click', board.clear)