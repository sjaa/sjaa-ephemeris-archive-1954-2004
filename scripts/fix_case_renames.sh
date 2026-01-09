#!/bin/bash

# Fix files that were renamed in filesystem but not properly in Git
# Uses intermediate rename to handle case-only changes on case-insensitive filesystems

files=(
"./Naughts/0112/EphDec01.pdf"
"./Naughts/0311/EphNov03.pdf"
"./Naughts/0310/EphOct03.pdf"
"./Naughts/0405/EphMay04A.pdf"
"./Naughts/0405/EphMay04.pdf"
"./Naughts/0402/EphFeb04.pdf"
"./Naughts/0003/EphMar00.pdf"
"./Naughts/0004/EphApr00.pdf"
"./Naughts/0209/EphSep02.pdf"
"./Naughts/0207/EphJul02.pdf"
"./Naughts/0403/EphMar04.pdf"
"./Naughts/0404/EphApr04.pdf"
"./Naughts/0206/EphJun02.pdf"
"./Naughts/0201/EphJan02.pdf"
"./Naughts/0005/EphMay00.pdf"
"./Naughts/0208/EphAug02.pdf"
"./Naughts/0002/EphFeb00.pdf"
"./Naughts/0212/EphDec02.pdf"
"./Naughts/0011/EphNov00.pdf"
"./Naughts/0410/EphOct04.pdf"
"./Naughts/0010/EphOct00.pdf"
"./Naughts/0411/EphNov04.pdf"
"./Naughts/0303/EphMar03.pdf"
"./Naughts/0109/EphSep01.pdf"
"./Naughts/0304/EphApr03.pdf"
"./Naughts/0107/EphJul01.pdf"
"./Naughts/0106/EphJun01.pdf"
"./Naughts/0101/EphJan01.pdf"
"./Naughts/0108/EphAug01.pdf"
"./Naughts/0305/EphMay03.pdf"
"./Naughts/0302/EphFeb03.pdf"
"./Naughts/0111/EphNov01.pdf"
"./Naughts/0312/EphDec03.pdf"
"./Naughts/0110/EphOct01.pdf"
"./Naughts/0007/EphJul00.pdf"
"./Naughts/0204/EphApr02.pdf"
"./Naughts/0009/EphSep00.pdf"
"./Naughts/0203/EphMar02.pdf"
"./Naughts/0401/EphJan04.pdf"
"./Naughts/0406/EphJun04.pdf"
"./Naughts/0408/EphAug04.pdf"
"./Naughts/0202/EphFeb02.pdf"
"./Naughts/0205/EphMay02.pdf"
"./Naughts/0008/EphAug00.pdf"
"./Naughts/0001/EphJan00.pdf"
"./Naughts/0006/EphJun00.pdf"
"./Naughts/0409/EphSep04.pdf"
"./Naughts/0407/EphJul04.pdf"
"./Naughts/0211/EphNov02.pdf"
"./Naughts/0012/EphDec00.pdf"
"./Naughts/0412/EphDec04.pdf"
"./Naughts/0210/EphOct02.pdf"
"./Naughts/0307/EphJul03.pdf"
"./Naughts/0309/EphSep03.pdf"
"./Naughts/0104/EphApr01.pdf"
"./Naughts/0103/EphMar01.pdf"
"./Naughts/0102/EphFeb01.pdf"
"./Naughts/0308/EphAug03.pdf"
"./Naughts/0105/EphMay01.pdf"
"./Naughts/0301/EphJan03.pdf"
"./Naughts/0306/EphJun03.pdf"
"./Nineties/9912/EphDec99.pdf"
"./Nineties/9909/EphSep99.pdf"
"./Nineties/9908/EphAug99.pdf"
"./Nineties/9911/EphNov99.pdf"
"./Nineties/9910/EphOct99.pdf"
"./Seventies/SJAA_AofI_Amend.pdf"
"./Fifties/SJAA_Article_of_Inc.pdf"
)

echo "Fixing ${#files[@]} files with case-only rename issues..."

for file in "${files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "Warning: File not found: $file"
        continue
    fi

    # Get directory and filename
    dir=$(dirname "$file")
    base=$(basename "$file" .pdf)

    # Create temporary filename
    temp="${dir}/${base}_TEMP.pdf"
    final="${dir}/${base}.pdf"

    echo ""
    echo "Processing: $file"

    # Step 1: Move to temporary name and commit
    echo "  Step 1: Renaming to temporary file..."
    git mv "$file" "$temp" 2>/dev/null || {
        echo "  Warning: git mv failed, trying regular mv + add"
        mv "$file" "$temp"
        git add "$temp"
    }

    # Step 2: Move to final lowercase name
    echo "  Step 2: Renaming to final lowercase name..."
    git mv "$temp" "$final" 2>/dev/null || {
        echo "  Warning: git mv failed for final rename, trying regular mv + add"
        mv "$temp" "$final"
        git add "$final"
    }

    echo "  ✓ Completed: $final"
done

echo ""
echo "All files processed. Please review with 'git status' and commit the changes."
