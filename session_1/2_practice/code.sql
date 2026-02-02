-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here
Select books.title, members.name, loans.loan_date from books, members, loans
Where loans.member_id = members.id and loans.book_id = books.id;

Select books.title, loans.id from books
left join loans on books.id = loans.book_id
Order By loans.id Asc;

Select librarybranch.name, librarybranch.id, books.title, books.id from librarybranch
Left Join books on librarybranch.id = books.branch_id 
Where books.Branch_id = librarybranch.id
group by books.id;

Select librarybranch.name, librarybranch.id, count(books.title) from librarybranch
Left Join books on librarybranch.id = books.branch_id 
Where books.Branch_id = librarybranch.id
group by librarybranch.id;

Select librarybranch.name, librarybranch.id, count(books.title) from books, librarybranch
Where books.Branch_id = librarybranch.id
group by librarybranch.id
having count(books.title) > 7;

Select members.id, members.name, count(loans.id) from members
left join loans on loans.member_id = members.id
Group By members.id;

Select members.id, members.name, count(loans.id) from members
left join loans on loans.member_id = members.id
Group By members.id
Having count(loans.id) = 0;

Select librarybranch.id, librarybranch.name, count(loans.id) from librarybranch, books
Left Join loans on loans.book_id = books.id and books.branch_id = librarybranch.id
Group By librarybranch.id;

Select members.id, members.name, count(loans.id) from members, loans
Where members.id = loans.member_id
Group By members.id;

Select books.id, books.title, loans.id, CASE WHEN loans.id IS NULL THEN 'Unloaned book' ELSE 'Loaned book' END as status from books
Left Join loans on books.id = loans.book_id
Order By books.id;