SELECT b.title, b.board_id, r.reply_id, r.writer_id, r.contents,
       DATE_FORMAT(r.created_date, '%Y-%m-%d') as CREATED_DATE
FROM used_goods_board b, used_goods_reply r
WHERE b.board_id = r.board_id AND b.created_date LIKE '%2022-10%'
ORDER BY r.created_date, b.title;
