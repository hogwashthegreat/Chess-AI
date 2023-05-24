var config = {
  draggable: true,
  position: 'start',
  onDrop: onDrop,
  sparePieces: true
}
var board = Chessboard('board1', config)

function clickShowPositionBtn () {
  console.log('Current position as an Object:')
  console.log(board.position())

  console.log('Current position as a FEN string:')
  console.log(board.fen())
  document.getElementById("updatingfen").innerHTML=board.fen();
}

function onDrop (source, target, piece, newPos, oldPos, orientation) {
  console.log('Source: ' + source)
  console.log('Target: ' + target)
  console.log('Piece: ' + piece)
  console.log('New position: ' + Chessboard.objToFen(newPos))
  console.log('Old position: ' + Chessboard.objToFen(oldPos))
  console.log('Orientation: ' + orientation)
  console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
}

$('#clearBtn').on('click', board.clear)

$('#startBtn').on('click', board.start)

$('#showPositionBtn').on('click', clickShowPositionBtn)