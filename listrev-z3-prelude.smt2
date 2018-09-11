(define-sort Set (T) (Array T Bool))

(define-sort Loc () Int)

;; list, list2, hlist, hlist2, key, keys, keys2
(declare-fun list (Loc) Bool)
(declare-fun list2 (Loc) Bool)
(declare-fun hlist (Loc) (Set Loc))
(declare-fun hlist2 (Loc) (Set Loc))
(declare-fun key (Loc) Int)
(declare-fun keys (Loc) (Set Int))
(declare-fun keys2 (Loc) (Set Int))

(declare-fun next (Loc) (Loc))

(declare-const nil Loc)
(assert (= nil -1))

(declare-const kk (Set Int))

(declare-const orig Loc)
(declare-const rev Loc)
(declare-const tmp Loc)
(declare-const orig2 Loc)
(declare-const rev2 Loc)

(declare-const a Loc)
